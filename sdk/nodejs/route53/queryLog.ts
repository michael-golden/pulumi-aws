// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a Route53 query logging configuration resource.
 * 
 * > **NOTE:** There are restrictions on the configuration of query logging. Notably,
 * the CloudWatch log group must be in the `us-east-1` region,
 * a permissive CloudWatch log resource policy must be in place, and
 * the Route53 hosted zone must be public.
 * See [Configuring Logging for DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring) for additional details.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_query_log.html.markdown.
 */
export class QueryLog extends pulumi.CustomResource {
    /**
     * Get an existing QueryLog resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueryLogState, opts?: pulumi.CustomResourceOptions): QueryLog {
        return new QueryLog(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:route53/queryLog:QueryLog';

    /**
     * Returns true if the given object is an instance of QueryLog.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is QueryLog {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === QueryLog.__pulumiType;
    }

    /**
     * CloudWatch log group ARN to send query logs.
     */
    public readonly cloudwatchLogGroupArn!: pulumi.Output<string>;
    /**
     * Route53 hosted zone ID to enable query logs.
     */
    public readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a QueryLog resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: QueryLogArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: QueryLogArgs | QueryLogState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as QueryLogState | undefined;
            inputs["cloudwatchLogGroupArn"] = state ? state.cloudwatchLogGroupArn : undefined;
            inputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as QueryLogArgs | undefined;
            if (!args || args.cloudwatchLogGroupArn === undefined) {
                throw new Error("Missing required property 'cloudwatchLogGroupArn'");
            }
            if (!args || args.zoneId === undefined) {
                throw new Error("Missing required property 'zoneId'");
            }
            inputs["cloudwatchLogGroupArn"] = args ? args.cloudwatchLogGroupArn : undefined;
            inputs["zoneId"] = args ? args.zoneId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(QueryLog.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering QueryLog resources.
 */
export interface QueryLogState {
    /**
     * CloudWatch log group ARN to send query logs.
     */
    readonly cloudwatchLogGroupArn?: pulumi.Input<string>;
    /**
     * Route53 hosted zone ID to enable query logs.
     */
    readonly zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a QueryLog resource.
 */
export interface QueryLogArgs {
    /**
     * CloudWatch log group ARN to send query logs.
     */
    readonly cloudwatchLogGroupArn: pulumi.Input<string>;
    /**
     * Route53 hosted zone ID to enable query logs.
     */
    readonly zoneId: pulumi.Input<string>;
}
