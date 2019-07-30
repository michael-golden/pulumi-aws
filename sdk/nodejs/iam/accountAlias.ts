// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * > **Note:** There is only a single account alias per AWS account.
 * 
 * Manages the account alias for the AWS Account.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const alias = new aws.iam.AccountAlias("alias", {
 *     accountAlias: "my-account-alias",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_alias.html.markdown.
 */
export class AccountAlias extends pulumi.CustomResource {
    /**
     * Get an existing AccountAlias resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountAliasState, opts?: pulumi.CustomResourceOptions): AccountAlias {
        return new AccountAlias(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:iam/accountAlias:AccountAlias';

    /**
     * Returns true if the given object is an instance of AccountAlias.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccountAlias {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccountAlias.__pulumiType;
    }

    /**
     * The account alias
     */
    public readonly accountAlias!: pulumi.Output<string>;

    /**
     * Create a AccountAlias resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccountAliasArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AccountAliasArgs | AccountAliasState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AccountAliasState | undefined;
            inputs["accountAlias"] = state ? state.accountAlias : undefined;
        } else {
            const args = argsOrState as AccountAliasArgs | undefined;
            if (!args || args.accountAlias === undefined) {
                throw new Error("Missing required property 'accountAlias'");
            }
            inputs["accountAlias"] = args ? args.accountAlias : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AccountAlias.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AccountAlias resources.
 */
export interface AccountAliasState {
    /**
     * The account alias
     */
    readonly accountAlias?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AccountAlias resource.
 */
export interface AccountAliasArgs {
    /**
     * The account alias
     */
    readonly accountAlias: pulumi.Input<string>;
}
