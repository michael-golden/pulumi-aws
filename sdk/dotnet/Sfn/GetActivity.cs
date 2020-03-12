// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Sfn
{
    public static partial class Invokes
    {
        /// <summary>
        /// Provides a Step Functions Activity data source
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/sfn_activity.html.markdown.
        /// </summary>
        public static Task<GetActivityResult> GetActivity(GetActivityArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetActivityResult>("aws:sfn/getActivity:getActivity", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetActivityArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) that identifies the activity.
        /// </summary>
        [Input("arn")]
        public string? Arn { get; set; }

        /// <summary>
        /// The name that identifies the activity.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetActivityArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetActivityResult
    {
        public readonly string Arn;
        /// <summary>
        /// The date the activity was created.
        /// </summary>
        public readonly string CreationDate;
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetActivityResult(
            string arn,
            string creationDate,
            string name,
            string id)
        {
            Arn = arn;
            CreationDate = creationDate;
            Name = name;
            Id = id;
        }
    }
}