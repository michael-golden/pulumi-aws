// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws
{
    public static partial class Invokes
    {
        /// <summary>
        /// The Canonical User ID data source allows access to the [canonical user ID](http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html)
        /// for the effective account in which this provider is working.  
        /// 
        /// 
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/canonical_user_id.html.markdown.
        /// </summary>
        [Obsolete("Use GetCanonicalUserId.InvokeAsync() instead")]
        public static Task<GetCanonicalUserIdResult> GetCanonicalUserId(InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCanonicalUserIdResult>("aws:index/getCanonicalUserId:getCanonicalUserId", InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetCanonicalUserId
    {
        /// <summary>
        /// The Canonical User ID data source allows access to the [canonical user ID](http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html)
        /// for the effective account in which this provider is working.  
        /// 
        /// 
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/canonical_user_id.html.markdown.
        /// </summary>
        public static Task<GetCanonicalUserIdResult> InvokeAsync(InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCanonicalUserIdResult>("aws:index/getCanonicalUserId:getCanonicalUserId", InvokeArgs.Empty, options.WithVersion());
    }

    [OutputType]
    public sealed class GetCanonicalUserIdResult
    {
        /// <summary>
        /// The human-friendly name linked to the canonical user ID. The bucket owner's display name. **NOTE:** [This value](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTServiceGET.html) is only included in the response in the US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), EU (Ireland), and South America (São Paulo) regions.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetCanonicalUserIdResult(
            string displayName,
            string id)
        {
            DisplayName = displayName;
            Id = id;
        }
    }
}
